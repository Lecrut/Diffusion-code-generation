class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, text):
        """
        Reverses the input string in-place if it is a list of characters,
        or returns a new reversed string if the input is already a str.

        Args:
            text (str | list[str]): The string or character list to reverse.

        Returns:
            str: A new string with characters in reverse order.
        """
        # Ensure we are working with a sequence of strings/characters
        if isinstance(text, str):
            return "".join(reversed(list(text)))
        elif isinstance(text, list) and all(isinstance(x, str) for x in text):
            reversed_list = []
            i = len(text) - 1
            while i >= 0:
                reversed_list.append(text[i])
                i -= 1
            return "".join(reversed_list)
        else:
            raise TypeError("Input must be a string or a list of strings.")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_cases = [
        "hello",
        ["h", "e", "l", "l", "o"],
        "",
        "Python Programming"
    ]

    reverser = StringReverser()

    for i, text in enumerate(test_cases):
        try:
            result = reverser.reverse(text)
            print(f"Test Case {i+1}:")
            if isinstance(text, str):
                print(f"  Input ({type(text).__name__}): '{text}' -> Output: '{result}'")
            else:
                input_str = "".join(text)
                output_str = result
                print(f"  Input list representation of string: '{input_str}' -> Reversed String: '{output_str}'")
        except Exception as e:
            print(f"Test Case {i+1}: Error occurred - {e}")