def file_streamer(file1, file2):
    for chunk in file1:
        yield chunk
    for chunk in file2:
        yield chunk
if __name__ == '__main__':
    import io
    data1 = b"This is the content of the first file.\n" + b"A much longer string to simulate a large file." * 100000
    data2 = b"This is the content of the second file, which is also quite long." + b"Another chunk for the second file." * 50000
    file1 = io.BytesIO(data1)
    file2 = io.BytesIO(data2)
    print("--- Streaming contents ---")
    for chunk in file_streamer(file1, file2):
        print(chunk)