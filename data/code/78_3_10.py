month_to_index = {
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

def month_difference(month1, month2):
    return abs(month_to_index[month1] - month_to_index[month2])

if __name__ == '__main__':
    print(month_difference('January', 'March'))