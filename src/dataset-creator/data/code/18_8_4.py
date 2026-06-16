import re
class SecureReverser:
    def validate_input(self, data):
        if not isinstance(data, str):
            raise TypeError("Input must be a string.")
        max_length = 1024 * 1024
        if len(data) > max_length:
            raise ValueError(f"Input length exceeds maximum allowed size of {max_length} characters.")
        forbidden_patterns = ['<script', 'javascript:', "onerror=", '<img' ]
        for pattern in forbidden_patterns:
            if re.search(pattern, data):
                raise SecurityError("Potentially malicious input detected.")
    def reverse_sequence(self, data):
        self.validate_input(data)
        return ''.join(reversed(list(data)))
class SecurityError(Exception):
    pass
if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "<script>alert('xss')</script>",
        "Normal text with numbers 12345"
    ]
    for case in test_cases:
        try:
            result = SecureReverser().reverse_sequence(case)
            print(f"Input: {case}")
            print(f"Output: {result}\n")
        except (TypeError, ValueError, SecurityError) as e:
            print(f"Input: {case}")
            print(f"Error: {e}\n")