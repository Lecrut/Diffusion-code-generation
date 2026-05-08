import math
def day_of_week_first_of_month(year, month):
    if month == 1:
        h = 1
        d = 0
    else:
        h = month
        d = 1
    k = year % 100
    j = year // 100
    q = 1
    m_zeller = month
    K = year % 100
    J = year // 100
    if m_zeller <= 2:
        m_zeller += 12
        year -= 1
    h = (q + math.floor(13 * (m_zeller + 1)) // 5 + K + math.floor(K / 4) + math.floor(J / 4) - 2 * J) % 7
    return h
if __name__ == '__main__':
    year1 = 2023
    month1 = 1
    result1 = day_of_week_first_of_month(year1, month1)
    print(f"Year: {year1}, Month: {month1}, Day of week for the 1st: {result1}")
    year2 = 2024
    month2 = 5
    result2 = day_of_week_first_of_month(year2, month2)
    print(f"Year: {year2}, Month: {month2}, Day of week for the 1st: {result2}")
    year3 = 2000
    month3 = 1
    result3 = day_of_week_first_of_month(year3, month3)
    print(f"Year: {year3}, Month: {month3}, Day of week for the 1st: {result3}")
    year4 = 1999
    month4 = 12
    result4 = day_of_week_first_of_month(year4, month4)
    print(f"Year: {year4}, Month: {month4}, Day of week for the 1st: {result4}")