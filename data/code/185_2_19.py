def split_log_entries(log_content, delimiter):
    return log_content.split(delimiter)

if __name__ == '__main__':
    sample_log = "2023-04-01 12:00:00 Error: System failure\n2023-04-01 12:05:00 Info: User logged in"
    delimiter = "\n"
    print(split_log_entries(sample_log, delimiter))