class HelloWorldRepeater:
    def repeat_message(self, message, count):
        return [message] * count

if __name__ == '__main__':
    repeater = HelloWorldRepeater()
    sample_message = 'Hello World'
    sample_count = 100
    repeated_messages = repeater.repeat_message(sample_message, sample_count)
    result = '\n'.join(repeated_messages)
    print(result)