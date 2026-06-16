def file_streamer(file1, file2):
    for chunk in file1:
        yield chunk
    for chunk in file2:
        yield chunk
if __name__ == '__main__':
    import io
    data1 = b"This is the content of the first file.\n" + b"A much longer string to simulate a large file." * 1000
    data2 = b"This is the content of the second file.\n" + b"Another long piece of data here." * 500
    file1 = io.BytesIO(data1)
    file2 = io.BytesIO(data2)
    stream = file_streamer(file1, file2)
    collected_data = bytearray()
    for chunk in stream:
        collected_data.extend(chunk)
    print("--- Collected Data ---")
    print(collected_data.decode('utf-8'))