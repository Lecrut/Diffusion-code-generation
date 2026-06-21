def split_log_entries(log_content: str, delimiter: str) -> list:
    return log_content.split(delimiter)

if __name__ == '__main__':
    sample_log = "2023-04-01 12:00:00 - Error: Connection failed\n2023-04-01 12:05:00 - Info: System rebooted"
    delimiter = "\n"
    print(split_log_entries(sample_log, delimiter))