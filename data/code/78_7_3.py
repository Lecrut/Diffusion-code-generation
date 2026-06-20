def month_difference(month1, month2):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    index1 = months.index(month1)
    index2 = months.index(month2)
    difference = abs(index1 - index2)
    return difference

if __name__ == '__main__':
    result = month_difference('March', 'November')
    print(result)