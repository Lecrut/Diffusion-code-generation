def km_to_meters(kilometers):
    return kilometers * 1000

def format_table(km_values):
    headers = ["Kilometers", "Meters"]
    rows = [[km, km_to_meters(km)] for km in km_values]
    
    col_widths = [
        max(len(str(row[col])) for row in [headers] + rows)
        for col in range(len(headers))
    ]
    
    def format_row(row):
        return " | ".join(str(item).rjust(width) for item, width in zip(row, col_widths))
    
    separator = "-+-".join("-" * width for width in col_widths)
    
    lines = [
        format_row(headers),
        separator,
    ]
    lines.extend(format_row(row) for row in rows)
    return "\n".join(lines)

if __name__ == '__main__':
    test_cases = [0, 1, 2.5, 10, 100, 0.001, 1234.5678]
    print(format_table(test_cases))