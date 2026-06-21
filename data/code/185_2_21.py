def split_log_entries(log_content):
    entries = log_content.split('Timestamp: ')
    cleaned_entries = []
    for entry in entries:
        if entry.strip():
            lines = entry.split('\n')
            if len(lines) > 1:
                cleaned_entry = '\n'.join(lines[1:])
                cleaned_entries.append(cleaned_entry.strip())
    return cleaned_entries

if __name__ == '__main__':
    log_content = "Timestamp: [2023-04-01 12:00:00]\nUser logged in\nTimestamp: [2023-04-01 12:05:00]\nUser performed action\nTimestamp: [2023-04-01 12:10:00]\nSession ended"
    split_entries = split_log_entries(log_content)
    for entry in split_entries:
        print(entry)