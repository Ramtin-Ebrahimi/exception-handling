class My_Exception(Exception) :
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"Error is : {self.message}..."
    

def avgValidate(avg):
	if not isinstance(avg,float):
		raise My_Exception("Type_error")
	if avg<10 or 25<avg:
		raise My_Exception("Out of range_error")
	return avg

	


try:
	avg=avgValidate(20)
	print(f"avg is : {avg}")
except My_Exception as error:
	print(error)
    


