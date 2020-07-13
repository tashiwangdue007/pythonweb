def application(environ, start_response):
	status ='200 OK'
	output = b'Hellow World -testing New pipeline for Python Modified complete automation'

	response_headers = [('Content-type', 'text/plain'),
			    ('Content-Length', str(len(output)))]

	start_response(status, response_headers)

	return [output]

