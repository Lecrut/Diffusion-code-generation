def month_difference(months, start_month, end_month):
    return months.index(end_month) - months.index(start_month)

if __name__ == '__main__':
    sample_months = ['January', 'February', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November', 'December']
    start = 'March'
    end = 'November'
    print(month_difference(sample_months, start, end))