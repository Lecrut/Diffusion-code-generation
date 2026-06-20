def month_difference(month1, month2):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    index1 = months.index(month1)
    index2 = months.index(month2)
    return abs(index1 - index2)
if __name__ == '__main__':
    print(month_difference('January', 'March'))
    print(month_difference('December', 'February'))