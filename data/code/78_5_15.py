def month_difference(months_list, start_month, end_month):
    start_index = months_list.index(start_month)
    end_index = months_list.index(end_month)
    return abs(end_index - start_index)

if __name__ == '__main__':
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    print(month_difference(months, 'March', 'November'))