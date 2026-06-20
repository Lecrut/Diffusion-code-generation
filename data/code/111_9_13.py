def format_date(date_str):
    month_names = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return f"{date_obj.day} {month_names[date_obj.month]} {date_obj.year}"

if __name__ == '__main__':
    sample_date = "2022-11-11"
    result = format_date(sample_date)
    print(result)