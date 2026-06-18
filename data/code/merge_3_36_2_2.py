class StringReverser:
    def reverse(self, text):
        """
        Reverses a given string in place by building a new reversed string using slicing.
        
        Args:
            text (str): The input string to be reversed.
            
        Returns:
            str: A new string that is the reverse of the input.
        """
        return text[::-1]

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no user input required
    tester = StringReverser()

    print("Test 1:", tester.reverse("Hello World"))   # Output: dlroW olleH
    print("Test 2:", tester.reverse(""))            # Output: (empty string)
    print("Test 3:", tester.reverse("Python is fun"))# Output: nuf si nohtyP