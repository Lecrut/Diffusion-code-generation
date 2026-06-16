import re
class TextProcessor:
    def __init__(self):
        self.cache = {}
    def count_words(self, text):
        words = set()
        for word in re.findall(r'\b\w+\b', text.lower()):
            if len(word) > 2 and not any(c.isdigit() or c.isupper() for c in word):
                words.add(word)
        return list(words), len(text.split())
    def find_patterns(self, text, pattern_type='email'):
        patterns = {
            'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            'phone': r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b',
            'url': r'https?://[^\s<>"{}|\\^`\[\]]+',
        }
        regex = patterns.get(pattern_type, None)
        if not regex:
            return []
        matches = re.findall(regex, text)
        self.cache[pattern_type] = len(matches)
        return matches
    def summarize(self, text):
        words, total_count = self.count_words(text)
        summary = f"Total unique meaningful words found: {len(words)}. Total word count in document: {total_count}."
        if 'email' not in [k for k, v in self.cache.items()]:
            email_matches = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
            summary += f"Email addresses detected: {len(email_matches)}."
        return summary
if __name__ == '__main__':
    sample_text = "Contact us at support@example.com or call 555-123-4567. Visit https://www.example.org for more info about our services and products."
    processor = TextProcessor()
    unique_words, total_count = processor.count_words(sample_text)
    emails = processor.find_patterns("email")
    phones = processor.find_patterns("phone")
    print(f"Unique Words: {unique_words}")
    print(f"Total Count: {total_count}")
    print(f"Emails Found: {emails}")
    print(f"Phones Found: {phones}")
    summary = processor.summarize(sample_text)
    print(summary)