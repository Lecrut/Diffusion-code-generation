def split_log_entries(log_content: str, delimiter: str) -> list:
    return log_content.split(delimiter)

if __name__ == '__main__':
    sample_log = "2023-01-01 12:00:00 INFO User logged in\n2023-01-01 12:05:00 ERROR File not found\n2023-01-01 12:10:00 INFO User logged out"
    delimiter = "\n"
    print(split_log_entries(sample_log, delimiter))