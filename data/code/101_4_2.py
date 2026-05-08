import math
def day_of_week_first_of_month(year, month):
    if month == 1:
        h = 1
        d = 1
    else:
        h = 1
        d = month
    k = year % 100
    j = year // 100
    m = year % 100
    q = 1
    m_zeller = month if month > 2 else month + 12
    K = year % 100
    J = year // 100
    h = (q + math.floor((13 * (m_zeller + 1)) / 5) + K + math.floor(K / 4) + math.floor(J / 4) - 2 * J) % 7
    q = 1
    m_zeller = month if month > 2 else month + 12
    K = year % 100
    J = year // 100
    h_zeller = (q + math.floor((13 * (m_zeller + 1)) / 5) + K + math.floor(K / 4) + math.floor(J / 4) - 2 * J) % 7
    day_index = (h_zeller + 5) % 7
    return day_index
if __name__ == '__main__':
    year1 = 2023
    month1 = 1
    result1 = day_of_week_first_of_month(year1, month1)
    print(f"Year: {year1}, Month: {month1}, Day of week for the 1st: {result1}")
    year2 = 2024
    month2 = 3
    result2 = day_of_week_first_of_month(year2, month2)
    print(f"Year: {year2}, Month: {month2}, Day of week for the 1st: {result2}")
    year3 = 2000
    month3 = 1
    result3 = day_of_week_first_of_month(year3, month3)
    print(f"Year: {year3}, Month: {month3}, Day of week for the 1st: {result3}")