def month_difference(month_list, month1, month2):
    month_to_index = {month: i for i, month in enumerate(month_list)}
    if month1 not in month_to_index or month2 not in month_to_index:
        return None
    index1 = month_to_index[month1]
    index2 = month_to_index[month2]
    difference = abs(index1 - index2)
    return difference
if __name__ == '__main__':
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_a = "March"
    month_b = "November"
    result = month_difference(months, month_a, month_b)
    print(result)