def count_consonants(text):
    consonants = set(
        "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        "ĐĐđÞÞĐĐđÞÞ"
        "çÇšŠžŽýÝàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ"
        "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞß"
        "āăąćĉċđēėęěĝğġģĥħĩīĭįıĳĵķĸĺļľŀłńņňŉŋōŏőœŕŗřśŝşșŢťŧũūŭůűůŵŷźżž"
        "ĀĂĄĆĈĊČĐĒĔĖĘĚĜĞĠĢĤĦĨĪĬĮİĲĴĶĸĹĻĽĿŁŃŅŊŌŎŐŔŖŘŚŜŞȘŢȚŤŦŨŪŬŮŰŲŴŶŸŹŻŽ"
    )
    return sum(1 for char in text if char in consonants)

if __name__ == '__main__':
    sample_text = "Hello Wörld! 123 Čašež Ť"
    result = count_consonants(sample_text)
    print(result)