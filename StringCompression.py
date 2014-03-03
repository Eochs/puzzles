# Function to perform basic string compression using the counts of repeated
# characters. If compressed string is larger than original return original.
# Example: string "aabcccccaaa" -> "a2b1c5a3

def Compress(s):
   charArray = []
   countArray = []
   for c in s:
      if len(charArray) == 0:
	 charArray.append(c)
         countArray.append(1)
      # same char as previous
      elif c == charArray[-1]:
	 countArray[-1] += 1
      # different char from previous in string
      else:
	 charArray.append(c)
         countArray.append(1)
   # create compressed string
   compressedStr = ""
   for i in range(len(charArray)):
      compressedStr = compressedStr + charArray[i] + str(countArray[i]) 
   if len(s) < len(compressedStr):
      return s
   return compressedStr


# Testing

strToBeCompressed = "aabbgggggyyaa"
strRightlyCompressed = a2b2g5y2a2"

if Compress(strToBeCompressed) == strRightlyCompressed:
   print "test passed"
else:
   print "test failed"
