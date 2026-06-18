class StringAppender:
    def append(self, first_string: str, second_string: str) -> str:
        """Returns a new string formed by appending the second argument to the first."""
        return f"{first_string}{second_string}"

if __name__ == '__main__':
    app = StringAppender()
    result1 = app.append("Hello", "World")
    print(result1)
    
    result2 = app.append("Python is ", "great!")
    print(result2)