import sys
class ListHeadRetriever:
    def get_head(self, data_list):
        if not isinstance(data_list, list):
            raise TypeError("Input must be a list.")
        try:
            return next(iter(data_list))
        except StopIteration:
            pass
        raise ValueError("Collection is empty. Cannot retrieve head element.")
def main():
    sample_data = [10, 20, 30]
    retriever = ListHeadRetriever()
    try:
        result = retriever.get_head(sample_data)
        print(f"Head of list: {result}")
        empty_sample = []
        try:
            head_empty = retriever.get_head(empty_sample)
        except ValueError as e:
            print(f"Error with empty collection: {e}", file=sys.stderr)
    except Exception as ex:
        print(f"Unexpected error occurred: {ex}", file=sys.stderr)
if __name__ == '__main__':
    main()