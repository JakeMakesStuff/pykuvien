from pykuvien import Api

kuvien = Api(
    id_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik1UZERNRUkwTVVSRU5qVTFSVEZET1RZM01EVTVSRU5CTlRKRVFVRXhRamt3TnpNeVJFWTROdyJ9.eyJlbWFpbCI6ImtlbHdpbmdAa2VsbmV0Lm9yZyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuaWNrbmFtZSI6ImtlbHdpbmciLCJuYW1lIjoia2Vsd2luZ0BrZWxuZXQub3JnIiwicGljdHVyZSI6Imh0dHBzOi8vcy5ncmF2YXRhci5jb20vYXZhdGFyLzA1MDQzY2EyZjAyZjYzODcyYTNjNzNkNzI4MmY3NWM5P3M9NDgwJnI9cGcmZD1odHRwcyUzQSUyRiUyRmNkbi5hdXRoMC5jb20lMkZhdmF0YXJzJTJGa2UucG5nIiwidXBkYXRlZF9hdCI6IjIwMTgtMDEtMThUMDU6NTE6MDkuNDEyWiIsImlzcyI6Imh0dHBzOi8va3V2aWVuLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1YTRjMDYwNGNhMDBiZDI4OWQwYjIwYzYiLCJhdWQiOiJrdFJ6dVdQVzZMOEZiRFc3c0JGaUphMzRZbFd1RjNlMCIsImlhdCI6MTUxNjI1NDY2OSwiZXhwIjoxNTE2ODU5NDY5LCJhdF9oYXNoIjoiak9NRXJiS2lsWWVtcDN6RllkN252QSIsIm5vbmNlIjoiZGxTYzhLZ1F5a05OYUVQTiJ9.RzsI7gLOyZdknThQw1TtoAuN7-8SUhfeyLM48dikTc93d_pNfzoXA6jOxx1FABwn5xfuyMWPRGwXjK9ylT_RNg1r0t--ejQtvQa37gEgo12_jUf-WQd0k8oJEBnRJGqU1zQ5NeabWD4gpy8S_rhxfZZSx1lAcFf1hi1qvUPoC5tk3wxjcP1xwznIzByP-2t7ELsXwssizgz5bReixHU4SbZxQENQrsTS_bSuko5FW1Qg6eCyQmSH7LZEV6djnr74bwbNzj9Q8w6ruIEwnYpTl6eJhbotLT7T0HksPMwDxU4JX2bEAi3soLxhpV0SHhViV-61RGgKRUdLUNX3-Hf_WA',
    access_token='rloMMZQZ-GnZQSSLxWeInAQYvybqod4H')

print(kuvien.domains())
