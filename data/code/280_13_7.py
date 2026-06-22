def format_message(param):
    return f"Processed value: {param * 10}"

if __name__ == '__main__':
    values = [2, 4, 6, 8, 10]
    formatted_values = [format_message(v) for v in values]
    print(formatted_values)