def split_log_entries(log_content, delimiter):
    return log_content.split(delimiter)

if __name__ == '__main__':
    sample_log = "2023-04-01 12:00:00 INFO User logged in\n2023-04-01 12:05:00 ERROR Failed to load data"
    delimiter = "\n"
    print(split_log_entries(sample_log, delimiter))