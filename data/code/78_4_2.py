def month_to_index(month_name):
    mapping = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    return mapping.get(month_name)
if __name__ == '__main__':
    month1 = "January"
    month2 = "March"
    index1 = month_to_index(month1)
    index2 = month_to_index(month2)
    if index1 is not None and index2 is not None:
        difference = abs(index1 - index2)
        print(difference)
    else:
        print("One or both month names are invalid.")