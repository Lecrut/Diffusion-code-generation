def split_log_entries(log_content: str) -> list:
    delimiter = "Timestamp:"
    entries = log_content.split(delimiter)
    cleaned_entries = [entry.strip() for entry in entries if entry.strip()]
    return cleaned_entries

if __name__ == '__main__':
    sample_log_content = """
Timestamp: 2023-04-01T12:00:00Z
Error: Connection failed

Timestamp: 2023-04-01T12:05:00Z
Info: User logged in

Timestamp: 2023-04-01T12:10:00Z
Warning: Low disk space
"""
    print(split_log_entries(sample_log_content))