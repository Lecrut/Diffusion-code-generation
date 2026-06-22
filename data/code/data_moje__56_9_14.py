def generate_eight_times_table() -> list[str]:
    return [f"{i} x 8 = {i * 8}" for i in range(1, 11)]

if __name__ == "__main__":
    table_rows = generate_eight_times_table()
    for row in table_rows:
        print(row)