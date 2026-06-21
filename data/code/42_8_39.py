class StringBuilder:

    def __init__(self):
        self.parts = []

    def append(self, part):
        if not isinstance(part, str):
            raise ValueError('Part must be a string.')
        self.parts.append(part)

    def build(self, separator=''):
        return separator.join(self.parts)
if __name__ == '__main__':
    try:
        builder1 = StringBuilder()
        builder1.append('Hello')
        builder1.append('world')
        builder1.append('this')
        builder1.append('is')
        builder1.append('a')
        builder1.append('test')
        builder2 = StringBuilder()
        builder2.append('This')
        builder2.append('is')
        builder2.append('another')
        builder2.append('example')
        print(builder1.build())
        print(builder1.build(' '))
        print(builder1.build(','))
        print(builder2.build('-'))
        print(builder2.build('\n'))
    except ValueError as e:
        print(e)