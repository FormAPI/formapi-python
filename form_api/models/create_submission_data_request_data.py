# coding: utf-8

"""
    API v1

    FormAPI is a service that helps you fill out and sign PDF templates.  # noqa: E501

    OpenAPI spec version: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CreateSubmissionDataRequestData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'metadata': 'object',
        'auth_type': 'str',
        'auth_second_factor_type': 'str',
        'auth_phone_number_hash': 'str',
        'auth_session_started_at': 'str',
        'auth_user_id_hash': 'str',
        'auth_session_id_hash': 'str',
        'auth_username_hash': 'str',
        'name': 'str',
        'fields': 'list[str]',
        'email': 'str',
        'auth_provider': 'str',
        'order': 'int'
    }

    attribute_map = {
        'metadata': 'metadata',
        'auth_type': 'auth_type',
        'auth_second_factor_type': 'auth_second_factor_type',
        'auth_phone_number_hash': 'auth_phone_number_hash',
        'auth_session_started_at': 'auth_session_started_at',
        'auth_user_id_hash': 'auth_user_id_hash',
        'auth_session_id_hash': 'auth_session_id_hash',
        'auth_username_hash': 'auth_username_hash',
        'name': 'name',
        'fields': 'fields',
        'email': 'email',
        'auth_provider': 'auth_provider',
        'order': 'order'
    }

    def __init__(self, metadata=None, auth_type=None, auth_second_factor_type=None, auth_phone_number_hash=None, auth_session_started_at=None, auth_user_id_hash=None, auth_session_id_hash=None, auth_username_hash=None, name=None, fields=None, email=None, auth_provider=None, order=None):  # noqa: E501
        """CreateSubmissionDataRequestData - a model defined in OpenAPI"""  # noqa: E501

        self._metadata = None
        self._auth_type = None
        self._auth_second_factor_type = None
        self._auth_phone_number_hash = None
        self._auth_session_started_at = None
        self._auth_user_id_hash = None
        self._auth_session_id_hash = None
        self._auth_username_hash = None
        self._name = None
        self._fields = None
        self._email = None
        self._auth_provider = None
        self._order = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        if auth_type is not None:
            self.auth_type = auth_type
        if auth_second_factor_type is not None:
            self.auth_second_factor_type = auth_second_factor_type
        if auth_phone_number_hash is not None:
            self.auth_phone_number_hash = auth_phone_number_hash
        if auth_session_started_at is not None:
            self.auth_session_started_at = auth_session_started_at
        if auth_user_id_hash is not None:
            self.auth_user_id_hash = auth_user_id_hash
        if auth_session_id_hash is not None:
            self.auth_session_id_hash = auth_session_id_hash
        if auth_username_hash is not None:
            self.auth_username_hash = auth_username_hash
        if name is not None:
            self.name = name
        if fields is not None:
            self.fields = fields
        if email is not None:
            self.email = email
        if auth_provider is not None:
            self.auth_provider = auth_provider
        if order is not None:
            self.order = order

    @property
    def metadata(self):
        """Gets the metadata of this CreateSubmissionDataRequestData.  # noqa: E501


        :return: The metadata of this CreateSubmissionDataRequestData.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateSubmissionDataRequestData.


        :param metadata: The metadata of this CreateSubmissionDataRequestData.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def auth_type(self):
        """Gets the auth_type of this CreateSubmissionDataRequestData.  # noqa: E501


        :return: The auth_type of this CreateSubmissionDataRequestData.  # noqa: E501
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this CreateSubmissionDataRequestData.


        :param auth_type: The auth_type of this CreateSubmissionDataRequestData.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "password", "oauth", "email_link", "phone_number", "ldap", "saml"]  # noqa: E501
        if auth_type not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_type` ({0}), must be one of {1}"  # noqa: E501
                .format(auth_type, allowed_values)
            )

        self._auth_type = auth_type

    @property
    def auth_second_factor_type(self):
        """Gets the auth_second_factor_type of this CreateSubmissionDataRequestData.  # noqa: E501


        :return: The auth_second_factor_type of this CreateSubmissionDataRequestData.  # noqa: E501
        :rtype: str
        """
        return self._auth_second_factor_type

    @auth_second_factor_type.setter
    def auth_second_factor_type(self, auth_second_factor_type):
        """Sets the auth_second_factor_type of this CreateSubmissionDataRequestData.


        :param auth_second_factor_type: The auth_second_factor_type of this CreateSubmissionDataRequestData.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "phone_number", "totp", "mobile_push", "security_key", "fingerprint"]  # noqa: E501
        if auth_second_factor_type not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_second_factor_type` ({0}), must be one of {1}"  # noqa: E501
                .format(auth_second_factor_type, allowed_values)
            )

        self._auth_second_factor_type = auth_second_factor_type

    @property
    def auth_phone_number_hash(self):
        """Gets the auth_phone_number_hash of this CreateSubmissionDataRequestData.  # noqa: E501


        :return: The auth_phone_number_hash of this CreateSubmissionDataRequestData.  # noqa: E501
        :rtype: str
        """
        return self._auth_phone_number_hash

    @auth_phone_number_hash.setter
    def auth_phone_number_hash(self, auth_phone_number_hash):
        """Sets the auth_phone_number_hash of this CreateSubmissionDataRequestData.


        :param auth_phone_number_hash: The auth_phone_number_hash of this CreateSubmissionDataRequestData.  # noqa: E501
        :type: str
        """

        self._auth_phone_number_hash = auth_phone_number_hash

    @property
    def auth_session_started_at(self):
        """Gets the auth_session_started_at of this CreateSubmissionDataRequestData.  # noqa: E501


        :return: The auth_session_started_at of this CreateSubmissionDataRequestData.  # noqa: E501
        :rtype: str
        """
        return self._auth_session_started_at

    @auth_session_started_at.setter
    def auth_session_started_at(self, auth_session_started_at):
        """Sets the auth_session_started_at of this CreateSubmissionDataRequestData.


        :param auth_session_started_at: The auth_session_started_at of this CreateSubmissionDataRequestData.  # noqa: E501
        :type: str
        """

        self._auth_session_started_at = auth_session_started_at

    @property
    def auth_user_id_hash(self):
        """Gets the auth_user_id_hash of this CreateSubmissionDataRequestData.  # noqa: E501


        :return: The auth_user_id_hash of this CreateSubmissionDataRequestData.  # noqa: E501
        :rtype: str
        """
        return self._auth_user_id_hash

    @auth_user_id_hash.setter
    def auth_user_id_hash(self, auth_user_id_hash):
        """Sets the auth_user_id_hash of this CreateSubmissionDataRequestData.


        :param auth_user_id_hash: The auth_user_id_hash of this CreateSubmissionDataRequestData.  # noqa: E501
        :type: str
        """

        self._auth_user_id_hash = auth_user_id_hash

    @property
    def auth_session_id_hash(self):
        """Gets the auth_session_id_hash of this CreateSubmissionDataRequestData.  # noqa: E501


        :return: The auth_session_id_hash of this CreateSubmissionDataRequestData.  # noqa: E501
        :rtype: str
        """
        return self._auth_session_id_hash

    @auth_session_id_hash.setter
    def auth_session_id_hash(self, auth_session_id_hash):
        """Sets the auth_session_id_hash of this CreateSubmissionDataRequestData.


        :param auth_session_id_hash: The auth_session_id_hash of this CreateSubmissionDataRequestData.  # noqa: E501
        :type: str
        """

        self._auth_session_id_hash = auth_session_id_hash

    @property
    def auth_username_hash(self):
        """Gets the auth_username_hash of this CreateSubmissionDataRequestData.  # noqa: E501


        :return: The auth_username_hash of this CreateSubmissionDataRequestData.  # noqa: E501
        :rtype: str
        """
        return self._auth_username_hash

    @auth_username_hash.setter
    def auth_username_hash(self, auth_username_hash):
        """Sets the auth_username_hash of this CreateSubmissionDataRequestData.


        :param auth_username_hash: The auth_username_hash of this CreateSubmissionDataRequestData.  # noqa: E501
        :type: str
        """

        self._auth_username_hash = auth_username_hash

    @property
    def name(self):
        """Gets the name of this CreateSubmissionDataRequestData.  # noqa: E501


        :return: The name of this CreateSubmissionDataRequestData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSubmissionDataRequestData.


        :param name: The name of this CreateSubmissionDataRequestData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def fields(self):
        """Gets the fields of this CreateSubmissionDataRequestData.  # noqa: E501


        :return: The fields of this CreateSubmissionDataRequestData.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this CreateSubmissionDataRequestData.


        :param fields: The fields of this CreateSubmissionDataRequestData.  # noqa: E501
        :type: list[str]
        """

        self._fields = fields

    @property
    def email(self):
        """Gets the email of this CreateSubmissionDataRequestData.  # noqa: E501


        :return: The email of this CreateSubmissionDataRequestData.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateSubmissionDataRequestData.


        :param email: The email of this CreateSubmissionDataRequestData.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def auth_provider(self):
        """Gets the auth_provider of this CreateSubmissionDataRequestData.  # noqa: E501


        :return: The auth_provider of this CreateSubmissionDataRequestData.  # noqa: E501
        :rtype: str
        """
        return self._auth_provider

    @auth_provider.setter
    def auth_provider(self, auth_provider):
        """Sets the auth_provider of this CreateSubmissionDataRequestData.


        :param auth_provider: The auth_provider of this CreateSubmissionDataRequestData.  # noqa: E501
        :type: str
        """

        self._auth_provider = auth_provider

    @property
    def order(self):
        """Gets the order of this CreateSubmissionDataRequestData.  # noqa: E501


        :return: The order of this CreateSubmissionDataRequestData.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CreateSubmissionDataRequestData.


        :param order: The order of this CreateSubmissionDataRequestData.  # noqa: E501
        :type: int
        """

        self._order = order

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateSubmissionDataRequestData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
