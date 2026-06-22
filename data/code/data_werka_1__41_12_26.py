class StringManipulator:
    @staticmethod
    def to_lowercase(s):
        return s.lower()

    @staticmethod
    def to_uppercase(s):
        return s.upper()

    @staticmethod
    def to_title_case(s):
        return s.title()

if __name__ == '__main__':
    sample_text = "Alibaba Cloud String Manipulation"
    lowercase_result = StringManipulator.to_lowercase(sample_text)
    uppercase_result = StringManipulator.to_uppercase(sample_text)
    titlecase_result = StringManipulator.to_title_case(sample_text)
    
    print("Original Text:", sample_text)
    print("Lowercase:", lowercase_result)
    print("Uppercase:", uppercase_result)
    print("Title Case:", titlecase_result)