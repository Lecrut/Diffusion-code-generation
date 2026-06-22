class HelloWorldRepeater:
    def repeat(self, times):
        result = ""
        for _ in range(times):
            result += "Hello World!\n"
        return result

if __name__ == '__main__':
    repeater = HelloWorldRepeater()
    print(repeater.repeat(10))