def parseInputFile(file):
    """
    Get all goodies info and number of employees

    :param file: Input file containing info about goodies and number of employees
    :return: number of employees and list of goodies
    """
    f = open(file)
    lines = f.readlines()
    f.close()

    # First line contains info about the number of employees
    numEmployees = int(lines[0].split(':')[1].strip('\n').strip(' '))
    goodies = []

    """
    From the 5th line goodies info is converted to dictionary of the form 
    {"name": <goodie_name>, "price": <goodie_price>}
    """
    for i in range(4, len(lines)):
        line = lines[i].split(':')
        goodie = {"name": line[0], "price": int(line[1].strip('\n').strip(' '))}
        goodies.append(goodie)

    return (numEmployees, goodies)


def writeOutputFile(file, goodies):
    """
    Write the goodies info that can be distributed to the output file

    :param file: Output file where the goodies info has to be written
    :param goodies: list of goodies
    :return: None
    """
    f = open(file, "w")
    f.write("The goodies selected for distribution are:\n\n")

    minPrice = goodies[0]["price"];
    maxPrice = goodies[0]["price"];

    for goodie in goodies:
        f.write(goodie["name"] + ": " + str(goodie["price"]) + "\n")

        if goodie["price"] < minPrice:
            minPrice = goodie["price"]
        
        if goodie["price"] > maxPrice:
            maxPrice = goodie["price"]

    f.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is " + str(maxPrice - minPrice) + "\n")


def selectGoodies(goodies, numEmployees):
    """
    Find out the goodies the HR team can distribute so that the
    difference between the low price goodie and the high price goodie selected is minimum.

    :param goodies: list of all goodies
    :param numEmployees: number of employees the goodies to be distributed
    :return:
    """
    if numEmployees > len(goodies):
        return []

    # Sort the goodies in non-decreasing order based on their price
    goodies = sorted(goodies, key=lambda goodie: goodie["price"])

    minDiff = goodies[numEmployees - 1]["price"] - goodies[0]["price"]
    startIdx = 0
    """
    Use a window of size numEmployees. Slide until the end of goodies list.
    At each iteration find the difference of the costliest and cheapest goodie in that
    window. Update minDiff if difference is less than minDiff
    """
    for i in range(1, len(goodies) - numEmployees + 1):
        currDiff = goodies[i + numEmployees - 1]["price"] - goodies[i]["price"]
        if currDiff < minDiff:
            startIdx = i
            minDiff = currDiff

    # Return the window with the minimum difference between costliest goodie and cheapest goodie
    return goodies[startIdx: startIdx + numEmployees]


def main():
    parsed = parseInputFile("inp.txt")
    numEmployees = parsed[0]
    goodies = parsed[1]

    selectedGoodies = selectGoodies(goodies, numEmployees)

    writeOutputFile("out.txt", selectedGoodies)


if __name__ == "__main__":
    main()
