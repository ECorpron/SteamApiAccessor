# Exception for when an unexpected response from an API is received
class InvalidResponseException(Exception):
    """Response Code is not 200"""
    pass
