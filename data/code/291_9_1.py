if __name__ == '__main__':
    string1 = "hello"
    string2 = "world"
    length1 = len(string1)
    length2 = len(string2)
    if length1 > length2:
        difference = length1 - length2
        print(f"{string1} has more characters than {string2} by {difference}")
    elif length2 > length1:
        difference = length2 - length1
        print(f"{string2} has more characters than {string1} by {difference}")
    else:
        print(f"{string1} and {string2} have the same number of characters")