def km_to_meters(kilometers):
    return kilometers * 1000

def format_table(km_values):
    results = [(km, km_to_meters(km)) for km in km_values]
    header = "{:<15} | {:<10}".format("Kilometers", "Meters")
    separator = "-" * len(header)
    lines = [header, separator]
    for km, meters in results:
        line = "{:<15} | {:<10}".format(km, meters)
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    test_cases = [1, 2.5, 10, 0, 100]
    table = format_table(test_cases)
    print(table)