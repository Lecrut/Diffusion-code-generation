def parse_comma_separated_csv(csv_string: str):
    return (item.strip() for item in csv_string.split(',') if item.strip())

if __name__ == '__main__':
    csv_data = "  apple , banana, , cherry ,  "
    result = list(parse_comma_separated_csv(csv_data))
    print(result)