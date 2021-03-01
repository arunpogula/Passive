from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
import paranoid


# With static_payload
@api_view()
def main(request):
    list_not_to_mask = ["id"]
    payload = {
    "id": 324324,
    "first_name": "Arun",
    "last_name": "kumar",
    "email": "Arun.kumar@abc.com"
}
    output_dict = payload
    for key in payload.keys():
        if key in list_not_to_mask:
            pass
        else:
            output_dict[key] = paranoid.maskGenerator(str(payload[key]), is_json=True)
    return Response(output_dict)


# With Dynamic_payload
@api_view(['GET','POST'])
def mask_view(request):
    input_dict = request.data['json']
    if request.method == 'POST':
        list_not_to_mask = ["id"]
        output_dict = input_dict
        for key in input_dict.keys():
            if key in list_not_to_mask:
                pass
            else:
                output_dict[key] = paranoid.maskGenerator(str(input_dict[key]), is_json=True)
    return Response(output_dict)