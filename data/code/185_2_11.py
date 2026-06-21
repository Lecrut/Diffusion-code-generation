def split_log_entries(log_content, delimiter):
    return log_content.split(delimiter)

if __name__ == '__main__':
    sample_log = "2023-10-01 08:00:00 Error: Something went wrong\n2023-10-01 09:00:00 Info: Process completed"
    delimiter = "\n"
    log_entries = split_log_entries(sample_log, delimiter)
    print(log_entries)