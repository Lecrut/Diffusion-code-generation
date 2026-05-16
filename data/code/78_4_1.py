def month_to_index(month_name):
    month_map = {
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
    return month_map.get(month_name)
if __name__ == '__main__':
    month1 = "March"
    month2 = "November"
    index1 = month_to_index(month1)
    index2 = month_to_index(month2)
    if index1 is not None and index2 is not None:
        difference = abs(index1 - index2)
        print(difference)
    else:
        print("One or both month names are invalid.")