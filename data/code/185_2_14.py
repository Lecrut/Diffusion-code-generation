LOG_DELIMITER = "Timestamp:"

def split_log_entries(log_content):
    entries = log_content.split(LOG_DELIMITER)
    cleaned_entries = [entry.strip() for entry in entries if entry]
    return cleaned_entries

if __name__ == '__main__':
    sample_log_content = """
Timestamp:2023-10-01 12:00:00
Error:File not found
Timestamp:2023-10-01 12:05:00
Warning:Low disk space
"""
    log_entries = split_log_entries(sample_log_content)
    print(log_entries)