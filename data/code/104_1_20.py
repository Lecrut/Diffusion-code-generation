def find_later_date(date_string_a: str, date_string_b: str) -> str:
    def extract_components(date_input: str) -> tuple:
        year_part = int(date_input[0:4])
        month_part = int(date_input[5:7])
        day_part = int(date_input[8:10])
        return (year_part, month_part, day_part)

    components_a = extract_components(date_string_a)
    components_b = extract_components(date_string_b)

    if components_a > components_b:
        return date_string_a
    if components_b > components_a:
        return date_string_b
    return date_string_a

if __name__ == '__main__':
    date_one = "2022-02-28"
    date_two = "2022-03-01"
    later = find_later_date(date_one, date_two)
    print(later)