
st = input()
lst = st.split(" ");
firstword = lst[0];
if(firstword[-1] == 'e'):
  print(lst[0] + 'x' + lst[1])
elif(firstword[-1] == 'x' and firstword[-2] == 'e'):
  print(lst[0] + lst[1])
elif(firstword[-1] == 'a' or firstword[-1] == 'i' or firstword[-1] == 'o' or firstword[-1] == 'u'):
  substr = firstword[0:len(lst[0])-1]
  print(substr + 'ex' + lst[1])
else:
  print(lst[0]+ 'ex' + lst[1])