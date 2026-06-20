def month_to_index(month_name):
    months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    return months.get(month_name, None)

def month_difference(month1, month2):
    index1 = month_to_index(month1)
    index2 = month_to_index(month2)
    if index1 is not None and index2 is not None:
        return abs(index1 - index2)
    else:
        return None
if __name__ == '__main__':
    print(month_difference('January', 'March'))
    print(month_difference('December', 'February'))
    print(month_difference('April', 'November'))