class FirstLetterExtractor:
    def extract_all(self, strings):
        """
        Extracts the first letter from each string in the input list.
        
        Args:
            strings (list[str]): A list of strings to process.
            
        Returns:
            list[str]: A list containing the first character of each non-empty string.
                       Empty strings or None values are skipped and not included in output.
        """
        result = []
        for s in strings:
            if isinstance(s, str) and len(s) > 0:
                result.append(s[0])
        return result

if __name__ == '__main__':
    sample_data = ["Hello", "World", "", "Python!", None]
    extractor = FirstLetterExtractor()
    output = extractor.extract_all(sample_data)
    print(output)