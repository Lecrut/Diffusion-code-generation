def month_difference(month1, month2):
    months = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    index1 = months.get(month1)
    index2 = months.get(month2)
    if index1 is None or index2 is None:
        raise ValueError("Invalid month name")
    return abs(index1 - index2)

if __name__ == '__main__':
    result = month_difference('March', 'November')
    print(result)