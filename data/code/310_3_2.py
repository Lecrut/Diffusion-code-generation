def file_streamer(file1, file2):
    for chunk in file1:
        yield chunk
    for chunk in file2:
        yield chunk
if __name__ == '__main__':
    import io
    data1 = b"This is the first large file content." * 1000000
    data2 = b"This is the second very large file content." * 1000000
    file1 = io.BytesIO(data1)
    file2 = io.BytesIO(data2)
    print("Starting stream...")
    for chunk in file_streamer(file1, file2):
        print(f"Yielded chunk size: {len(chunk)}")
    print("Stream finished.")