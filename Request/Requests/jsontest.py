from Request.request import Request
from Model.authentication import requirelogin
from Networking.statuscodes import StatusCodes as CODE
from Request.requesterrors import NotFound, ServerError, Unauthorised, MethodNotAllowed

class Jsontest(Request):

	def __init__(self,):
		super(Jsontest, self).__init__()

	@requirelogin
	def _doGet(self):
		rdata = {}
		rdata["error_code"] = 200
		rdata['message'] = "Test Call completed successfully"
		return self._response(rdata, CODE.OK)