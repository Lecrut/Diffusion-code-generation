from datetime import date

def get_day_of_month():
    days_mapping = {
        'October': 10
    }
    return days_mapping['October']

if __name__ == '__main__':
    print(get_day_of_month())