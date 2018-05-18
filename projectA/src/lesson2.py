def my_encodings(x): 
    encodings = ('Latin-1', 'CP1251', 'UTF-16')
    for i in range(3):
        t = x
        print(t.encode(encodings[i]))

def GetLongestWord(s):
    longest=""
    
    for w in s.split(" "):
        if len(w) > len(longest):
            longest = w
            continue
    return longest

x = input("Enter string: ")
#my_encodings(x)
print(GetLongestWord(x))
