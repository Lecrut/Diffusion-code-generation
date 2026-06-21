def split_log_entries(log_content, delimiter):
    cleaned_entries = []
    for entry in log_content.split(delimiter):
        if entry.strip():
            cleaned_entries.append(entry.strip())
    return cleaned_entries

if __name__ == '__main__':
    sample_log_content = "2023-04-01 12:00:00 Error message\n2023-04-01 12:05:00 Info log\n2023-04-01 12:10:00 Warning notice"
    delimiter = "\n"
    entries = split_log_entries(sample_log_content, delimiter)
    for entry in entries:
        print(entry)