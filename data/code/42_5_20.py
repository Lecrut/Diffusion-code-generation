class StringManipulator:

    def merge_fragments(self, fragments):
        if not fragments:
            return ''
        return ''.join(fragments)
if __name__ == '__main__':
    manipulator = StringManipulator()
    sample_fragments = ['Hello', ' ', 'World', '!']
    result = manipulator.merge_fragments(sample_fragments)
    print(result)