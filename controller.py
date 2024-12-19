def doorAutomate(state):
    if state == 0:
        print("Door is opening...")
    elif state == 1:
        print("Door is closing...")
    else:
        print("Invalid state.")


import sys
print(sys.path)


import sys
sys.path.insert(0, r"C:\Users\Harish.S\Desktop\face recognition")

from controller import doorAutomate