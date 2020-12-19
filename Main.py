from pythonping import ping
from datetime import datetime
from time import sleep


def get_config_dictionary(lines):
    words = []
    words_final = []
    config_dictionary = {}

    for line in lines:
        for word in line.split():
            words.append(word)

    print(words)

    for word in words:
        if not ("=" and "\"") in word and ("=" or "\"") != word:
            words_final.append(word)
        elif "\"" in word:
            word = word.strip("\"")
            words_final.append(word)

    isKey = True
    for wordFinal in words_final:
        if isKey:
            config_dictionary[wordFinal] = words_final[words_final.index(wordFinal) + 1]
            isKey = False
        else:
            isKey = True
    return config_dictionary


URL = ""
output = ""

Config = open("Pingy.conf", "r")
URL = get_config_dictionary(Config.readlines())["URL"]
print(URL)


while True:
    ConnectionLog = open("connection.log", "w")
    PingResult = ping(URL, verbose=True)

    if PingResult.success():
        PingSuccessful = "Successful"
    else:
        PingSuccessful = "not Successful"

    output = output + "\n" + PingSuccessful + " at " + str((datetime.now().strftime("%B %d, %Y : %H:%M:%S")))
    ConnectionLog.write(output)
    print(output)
    ConnectionLog.close()
    sleep(5)
