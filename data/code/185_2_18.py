class LogEntryParser:
    TIMESTAMP_DELIMITER = " - "

    @staticmethod
    def clean_entry(entry):
        return entry.strip()

    @classmethod
    def parse_log(cls, log_content):
        entries = log_content.split(cls.TIMESTAMP_DELIMITER)
        cleaned_entries = [cls.clean_entry(entry) for entry in entries if entry]
        return cleaned_entries

if __name__ == '__main__':
    sample_log_content = "2023-04-01 12:00:00 - Error: File not found\n2023-04-01 12:05:00 - Info: User logged in"
    parsed_entries = LogEntryParser.parse_log(sample_log_content)
    print(parsed_entries)