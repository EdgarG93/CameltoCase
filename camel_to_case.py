def camel_to_snake(string):		
	pattern = r"[A-Z]"
	finder = re.findall(pattern, string)
	if re.match(r"^[A-Z]", string):
		finder.pop(0)
	str_replace = ["_" + elem for elem in finder]
	i = 0
	while i < len (finder):
		string = string.replace(finder[i], str_replace[i])
		i+=1
	print(string.lower())
	
txt = str(input())
camel_to_snake(txt)
