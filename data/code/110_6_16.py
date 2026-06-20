class TimestampSorter:
    @staticmethod
    def sort_timestamps(timestamp_list):
        return sorted(timestamp_list)

if __name__ == '__main__':
    sample_timestamps = [1632938400, 1633021200, 1633111200, 1633024800]
    sorter = TimestampSorter()
    sorted_timestamps = sorter.sort_timestamps(sample_timestamps)
    print(sorted_timestamps)