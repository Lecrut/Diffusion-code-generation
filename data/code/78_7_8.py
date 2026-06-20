def month_difference(month1, month2):
    months = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }
    index1 = months[month1]
    index2 = months[month2]
    difference = abs(index1 - index2)
    return difference

if __name__ == '__main__':
    result = month_difference('March', 'November')
    print(result)