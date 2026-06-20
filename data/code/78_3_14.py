def calculate_month_difference(month1_name, month2_name):
    month_map = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}

    def get_month_index(month_name):
        try:
            return month_map[month_name.lower()]
        except KeyError:
            return None
    index1 = get_month_index(month1_name)
    index2 = get_month_index(month2_name)
    if index1 is None or index2 is None:
        return 'Invalid month name'
    difference = abs(index1 - index2)
    return difference
if __name__ == '__main__':
    print(calculate_month_difference('March', 'November'))
    print(calculate_month_difference('December', 'February'))
    print(calculate_month_difference('April', 'April'))